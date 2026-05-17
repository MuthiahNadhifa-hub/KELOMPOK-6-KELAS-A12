class GaussElimination:
    def __init__(self, A, b):
        '''
        A: Matriks Koefisien (list of list)
        b: Vektor konstanta (list)
        '''
        self.n = len(A)
        self.A = [row[:] for row in A]  #copy matrix
        self.b = b[:]
        self.steps = [] #menyimpan proses eliminasi

    def print_matrix(self):
        '''Menampilkan matriks augmented'''   
        print("Matriks saat ini: ")
        for i in range(self.n):
            print(self.A[i], "|", self.b[i])
        print()

    def forward_elimination(self):
        '''Eliminasi Maju'''
        for i in range(self.n):
            #Pivot (Jika nol, tukar baris)
            if self.A[i][i] == 0:
                for k in range(i + 1, self.n):
                    if self.A[k][i] != 0:
                        #tukar baris
                        self.A[i], self.A[k] = self.A[k], self.A[i]
                        self.b[i], self.b[k] = self.b[k], self.b[i]
                        break

            #Eliminasi
            for j in range(i + 1, self.n):
                ratio = self.A[j][i] / self.A[i][i]

                for k in range(self.n):
                    self.A[j][k] -= ratio * self.A[i][k]
                
                self.b[j] -= ratio * self.b[i]

                #simpan Langkah
                self.steps.append((i, j, ratio, [row[:] for row in self.A], self.b[:]))

        return self.A, self.b
    
    def back_substitution(self):
        '''Substitusi balik'''
        x = [0 for _ in range(self.n)]

        for i in range(self.n - 1, -1, -1):
            sum_ax = sum(self.A[i][j] * x[j] for j in range(i + 1, self.n))
            x[i] = (self.b[i] - sum_ax) / self.A[i][i]
        
        return x
    
    def show_steps(self):
        '''Menampilkan proses eliminasi'''
        print("Tahapan Eliminasi: ")
        for step in self.steps:
            i, j, ratio, A, b = step
            print(f"R{j+1} = R{j+1} - ({ratio:.2f}) * R{i+1}")
            for r in range(self.n):
                print(A[r], "|", b[r])
            print()

    def solve(self, show_process=True):
        '''Menjalankan seluruh proses'''
        if show_process:
            print("=== Matriks Awal ===")
            self.print_matrix()
        
        self.forward_elimination()

        if show_process:
            print("=== Setelah ELiminasi Maju ===")
            self.print_matrix()
            self.show_steps()

        solution = self.back_substitution()

        if show_process:
            print("=== Solusi Akhir ===")
            for i, val in enumerate(solution):
                print(f"x{i+1} = {val}")
        
        return solution
