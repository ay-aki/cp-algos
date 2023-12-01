
# Copyright (C) 2023 Akihiro Y. @ Tsukuba Univ. All rights reserved.



using LinearAlgebra, Random, CUDA



function jl_qr!(
      q, r, A
    ; is_cuda = (typeof(A) <: CuArray)
    , Matrix0 = if is_cuda CUDA.CuMatrix else Matrix end
)
    F  = qr(A)
    q .= Matrix0(F.Q)
    r .= F.R
end
function jl_bgmres_history(it, reslist, klist)
    return (
          it  = it
        , res = collect(reslist[1:it+1])
        , d   = [(reslist[i+1] - reslist[i]) for i = 1:(length(reslist)-1)]
        , k   = collect(klist[1:it+1])
    )
end
function jl_bgmres_history_0()
    return (it = 0, res = [], d = [], k = [])
end



"""
# Block-GMRES
GMRESのBlockバージョン。
リスタートが実装されている。
Givens-Rotationは実装していない。
## サンプル(1)
```
# サンプル
Random.seed!(1);
# Init
n, p = 300, 20;
A = rand(n, n); b = rand(n, p); x0 = zeros(n, p); 
dA = (m -> m'*m/10)(rand(n, n)); 
Pr = lu(A+dA); 
# Block-GMRES
@time _, hist = jl_bgmres(A, b, x0 = x0, m = 10, max_it = 100, Pr = Pr);
# check
hist.it, hist.res, hist.k, hist.d
hist.res[end] / norm(b)
```
## サンプル(2)
```
# サンプル
Random.seed!(1);
# Init
n, p = 300, 20;
A = CUDA.rand(n, n); b = CUDA.rand(n, p); x0 = CUDA.zeros(n, p); 
dA = (m -> m'*m/10)(CUDA.rand(n, n)); 
Pr = lu(A+dA); 
# Block-GMRES
@time _, hist = jl_bgmres(A, b, x0 = x0, m = 1, max_it = 100, Pr = Pr);
# check
hist.it, hist.res, hist.k, hist.d
hist.res[end] / norm(b)
```
"""
function jl_bgmres(
      A, b
    # Parameters
    ; n      = size(b,1)
    , p      = size(b,2)
    , Pr     = I
    , m      = 10
    , max_it = 10
    , tol    = 1e-5
    , tolh   = 1e-10
    # CUDA functions
    , is_cuda = (typeof(A) <: CuArray)
    , zeros0  = if is_cuda CUDA.zeros    else zeros  end
    , Matrix0 = if is_cuda CUDA.CuMatrix else Matrix end
    # Initialize
    , norm_b = norm(b)
    , tolb   = tol * norm_b
    , x0     = zeros0(n, p)
    , r0     = zeros0(n, p)
    , y      = zeros0(p*(m+1), p)
    , w      = zeros0(n, p)
    , h      = zeros0(p*(m+1), p*m)
    , v      = zeros0(n, p*(m+1))
    , β      = zeros0(p, p)
    , e1     = [Matrix0{Float64}(I, p, p); zeros0(m*p, p)]
    # History
    , reslist= ones(max_it+1) # i+1
    , klist  = zeros(Int16, max_it+1)
    # Index function
    , idx = i -> ( # rev
        if     typeof(i) <: Integer   
            return ((i-1)*p+1):(i*p)
        elseif typeof(i) <: UnitRange 
            return ((i[begin]-1)*p+1):(i[end]*p)
        end
    )
)
    # Initialize
    z = Pr \ b; if (norm(b - A*z) < tolb) x0 .= z; return x0, jl_bgmres_history_0() end
    # Iteration (Restart)
    it = 0; while true
        # Constract orth [v(1),v(2),...,v(m)]
        r0 .= b - A*x0 # residual
        jl_qr!(view(v,:,idx(1)), β, r0) # v(1)*β = r
        reslist[it+1] = norm_β = norm(β)
        if ((norm_β < tolb) | (it >= max_it)) break end # check convergence
        k = 1; for j = 1:m 
            # Gram-Schmidt
            w .= A * (Pr \ v[:,idx(j)])
            for i = 1:j
                h[idx(i),idx(j)] .= v[:,idx(i)]' * w
                w .= w - v[:,idx(i)] * h[idx(i),idx(j)]
            end
            jl_qr!(view(v,:,idx(j+1)), view(h,idx(j+1),idx(j)), w) # v(j)*h(j+1,j) = w
            if (norm(h[idx(j+1),idx(j)]) < tolh) k = j-1; break end # check convergence
        k = j; end
        # Update Approximation
        klist[it+2] = k
        y[idx(1:k),:] .= h[idx(1:k+1),idx(1:k)] \ (e1[idx(1:k+1),:] * β)
        x0 .= x0 + Pr \ (v[:,idx(1:k)] * y[idx(1:k),:])
    it += 1; end
    return x0, jl_bgmres_history(it, reslist, klist)
end



# サンプル
Random.seed!(1);
# Init
n, p = 300, 20;
A = CUDA.rand(n, n); b = CUDA.rand(n, p); x0 = CUDA.zeros(n, p); 
dA = (m -> m'*m/10)(CUDA.rand(n, n)); 
Pr = lu(A+dA); 
# Block-GMRES
@time _, hist = jl_bgmres(A, b, x0 = x0, m = 1, max_it = 100, Pr = Pr);
# check
hist.it, hist.res, hist.k, hist.d
hist.res[end] / norm(b)


