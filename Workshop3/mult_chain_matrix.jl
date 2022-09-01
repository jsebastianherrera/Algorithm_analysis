function MatrixChainBK(B,R,i,j)
  if i == j
    push!(R, "A"*string(i)*" ")
  else
    push!(R,"( ")
    q = B[i,j]
    MatrixChainBK(B,R,i,q)
    MatrixChainBK(B,R,q+1,j)
    push!(R,") ")
  end
end

function MatrixChainB(S)
  M = [0 for i = 1:length(S)-1,i=1:length(S)-1]
  B = [-1 for i = 1:length(S)-1,i=1:length(S)-1]
  
  for i in length(S) -1-1:-1:1
    for j in i+1:length(S)-1
      q = Inf
      m = 1
      for k in i:j-1
        l = M[i,k]
        r = M[k+1,j]
        v = l+r+(S[i]*S[k]*S[j])
        if v < q
          q = v
          m = k
        end
      end
      M[i,j] = q
      B[i,j] = m
    end
  end
  return M, B
end

D = [1, 2, 3,4,3]
_, B = MatrixChainB(D)
n=size(B)[1]
R = String[]
MatrixChainBK(B,R,1,n)

@show R

