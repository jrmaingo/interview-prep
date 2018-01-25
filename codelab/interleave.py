class Solution:
    def __init__(self):
        self.comp_table = None
        self.A = None
        self.B = None
        self.C = None

    def isInterleaveHelper(self, a_idx, b_idx, c_idx):
        #print(f"recurse next step for {repr(self.A)}, {repr(self.B)}, {repr(self.C)}")
        if len(self.A) + len(self.B) != len(self.C):
            #print("len don't match")
            return False

        a_idx_orig = a_idx
        b_idx_orig = b_idx
        c_idx_orig = c_idx

        while c_idx < len(self.C):
            if len(self.A) == a_idx:
                #print(f"comp {repr(self.B[b_idx:])} to {repr(self.C[c_idx:])}")
                #print(f"{a_idx}, {b_idx}, {c_idx}")
                if self.comp_table[a_idx][b_idx][c_idx] == None:
                    self.comp_table[a_idx][b_idx][c_idx] = self.B[b_idx:] == self.C[c_idx:]
                #print(f"{a_idx},{b_idx},{c_idx}: {self.comp_table[a_idx][b_idx][c_idx]}")
                return self.comp_table[a_idx][b_idx][c_idx]
            elif len(self.B) == b_idx:
                #print(f"comp {repr(self.A[a_idx:])} to {repr(self.C[c_idx:])}")
                if self.comp_table[a_idx][b_idx][c_idx] == None:
                    self.comp_table[a_idx][b_idx][c_idx] = self.A[a_idx:] == self.C[c_idx:]
                #print(f"{a_idx},{b_idx},{c_idx}: {self.comp_table[a_idx][b_idx][c_idx]}")
                return self.comp_table[a_idx][b_idx][c_idx]
            elif self.A[a_idx] != self.C[c_idx] and self.B[b_idx] != self.C[c_idx]:
                #print(f"no next step for {repr(self.A)}, {repr(self.B)}, {repr(self.C)}")
                self.comp_table[a_idx][b_idx][c_idx] = False
                #print(f"{a_idx},{b_idx},{c_idx}: {self.comp_table[a_idx][b_idx][c_idx]}")
                return False;
            elif self.A[a_idx] == self.B[b_idx]:
                if self.comp_table[a_idx + 1][b_idx][c_idx + 1] == None:
                    self.comp_table[a_idx + 1][b_idx][c_idx + 1] = self.isInterleaveHelper(a_idx + 1, b_idx, c_idx + 1)
                if self.comp_table[a_idx + 1][b_idx][c_idx + 1] == True:
                    return True
                elif self.comp_table[a_idx][b_idx + 1][c_idx + 1] == None:
                    self.comp_table[a_idx][b_idx + 1][c_idx + 1] = self.isInterleaveHelper(a_idx, b_idx + 1, c_idx + 1)
                return self.comp_table[a_idx][b_idx + 1][c_idx + 1]
            elif self.A[a_idx] == self.C[c_idx]:
                a_idx += 1
            elif self.B[b_idx] == self.C[c_idx]:
                b_idx += 1
            c_idx += 1

        self.comp_table[a_idx_orig][b_idx_orig][c_idx_orig] = True
        return True

    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        self.comp_table = [[[None for i in range(len(C) + 1)] for j in range(len(B) + 1)] for k in range(len(A) + 1)]
        #print(repr(self.comp_table))
        self.A = A
        self.B = B
        self.C = C
        return self.isInterleaveHelper(0, 0, 0)

s1 = "aabcc"
s2 = "dbbca"
#s3 = "aadbbcbcac"
s3 = "aadbbbaccc"
#s1 = "abc"
#s2 = "def"
#s3 = "adbecf"
sol = Solution()
print(sol.isInterleave(s1, s2, s3))
