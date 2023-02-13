import br.com.thiago.bytebank.LOG
import br.com.thiago.bytebank.modelo.Cliente
import br.com.thiago.modelo.ContaCorrente
import br.com.thiago.bytebank.modelo.ContaPoupanca
import br.com.thiago.bytebank.modelo.Endereco
import br.com.thiago.bytebank.modelo.totalContas

fun main() {
    LOG.info("Iniciando o sistema!")
    testaComportamentoConta()
}

fun testaComportamentoConta() {
    val thiago = Cliente(
        nome = "Thiago",
        cpf = "123456789",
        senha = 1,
        endereco = Endereco(logradouro = "Rua Nova Olinda"),
    )
    val contaCorrenteThiago = ContaCorrente(titular = thiago, numero = 1000)

    val fran = Cliente(nome = "Fran", cpf = "222222222", senha = 2)
    val contaPoupancaFran = ContaPoupanca(numero = 1001, titular = fran)

    println("Titular: ${contaCorrenteThiago.titular}")
    println("Numero da conta: ${contaCorrenteThiago.numero}")
    println("Saldo: R$ ${contaCorrenteThiago.saldo}")
    contaCorrenteThiago.deposita(valor = 0.0)
    println()

    println("Titular: ${contaPoupancaFran.titular}")
    println("Numero da conta: ${contaPoupancaFran.numero}")
    println("Saldo: R$ ${contaPoupancaFran.saldo}")
    contaPoupancaFran.deposita(valor = 300.0)

    println()
    contaCorrenteThiago.deposita(55.0)
    contaPoupancaFran.deposita(26.0)

    println()
    contaCorrenteThiago.saca(75.0)
    contaPoupancaFran.saca(200.0)

    println()
    contaCorrenteThiago.transfere(5.0, contaPoupancaFran)

    println("Total de contas é: $totalContas")
}