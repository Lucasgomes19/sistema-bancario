class Conta:
    def __init__(self, numero, titular, senha, saldo=0):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor, senha):
        if valor > 0 and self.saldo >= valor and self.senha == senha:
            self.saldo -= valor
            return True
        return False

    def consultar_saldo(self, senha):
        if self.senha == senha:
            return self.saldo
        return "Senha incorreta"

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular, senha):
        if numero not in self.contas:
            self.contas[numero] = Conta(numero, titular, senha)
            return True
        return False

    def depositar(self, numero, valor):
        if numero in self.contas:
            return self.contas[numero].depositar(valor)
        return False

    def sacar(self, numero, valor, senha):
        if numero in self.contas:
            return self.contas[numero].sacar(valor, senha)
        return False

    def consultar_saldo(self, numero, senha):
        if numero in self.contas:
            return self.contas[numero].consultar_saldo(senha)
        return "Conta não encontrada"

def main():
    meu_banco = Banco()
    meu_banco.criar_conta(12345, "Lucas", "senha123")
    meu_banco.depositar(12345, 500)
    saldo = meu_banco.consultar_saldo(12345, "senha123")
    print(f"Saldo após depósito: {saldo}")
    meu_banco.sacar(12345, 200, "senha123")
    saldo = meu_banco.consultar_saldo(12345, "senha123")
    print(f"Saldo após saque: {saldo}")
    if meu_banco.sacar(12345, 100, "senha_errada"):
        print("Saque realizado com sucesso!")
    else:
        print("Falha ao realizar saque - senha incorreta!")

if __name__ == "__main__":
    main()
