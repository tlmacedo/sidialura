import br.com.thiago.bytebank.modelo.Cliente
import br.com.thiago.bytebank.modelo.ContaPoupanca
import br.com.thiago.bytebank.modelo.totalContas
import br.com.thiago.modelo.*


fun main() {

    val thiago = Cliente(nome = "Thiago", cpf = "", senha = 1)
    val contaPoupanca = ContaPoupanca(titular = thiago, numero = 1)
    val contaCorrente = ContaCorrente(titular = Cliente(nome = "Carla", cpf = "", senha = 2), numero = 2)

    testaContasDiferentes()

    LOG."\nTotal de Contas: $totalContas")

}

fun testaContasDiferentes() {

    val thiago = Analista(
        nome = "Thiago Macedo",
        cpf = "123.456.789.00",
        salario = 1000.0
    )
    LOG.)
    LOG."nome: ${thiago.nome}")
    LOG."cpf: ${thiago.cpf}")
    LOG."salario: R$${thiago.salario}")
    LOG."bonificação: R$${thiago.getBonificacao()}")


    val fran = Gerente(
        nome = "Fran",
        cpf = "222.222.222-22",
        salario = 2000.0,
        senha = 1234
    )
    LOG.)
    LOG."nome: ${fran.nome}")
    LOG."cpf: ${fran.cpf}")
    LOG."salario: R$${fran.salario}")
    LOG."bonificação: R$${fran.getBonificacao()}")

    if (fran.autentica(1234)) {
        LOG."autenticou com sucesso")
    } else {
        LOG."não foi possivel autenticar")
    }


    val gui = Diretor(
        nome = "Gui",
        cpf = "333.333.333-33",
        salario = 4000.0,
        senha = 4000,
        plr = 200.0
    )
    LOG.)
    LOG."nome: ${gui.nome}")
    LOG."cpf: ${gui.cpf}")
    LOG."salario: R$${gui.salario}")
    LOG."bonificação: R$${gui.getBonificacao()}")
    LOG."plr: R$${gui.plr}")

    if (gui.autentica(4000)) {
        LOG."autenticou com sucesso")
    } else {
        LOG."não foi possivel autenticar")
    }

    //testaComportamentoConta()
    val calculadora = CalculadoraBonificacao()
    calculadora.registra(thiago)
    calculadora.registra(fran)
    calculadora.registra(gui)

    LOG."total de bonificação: R$${calculadora.total}")
}
