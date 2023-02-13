import br.com.thiago.modelo.Analista
import br.com.thiago.modelo.CalculadoraBonificacao
import br.com.thiago.modelo.Diretor
import br.com.thiago.modelo.Gerente

fun testaFuncionarios() {
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


    val maria = Analista(
        nome = "Maria",
        cpf = "444.444.444-44",
        salario = 3000.0,
    )
    LOG.)
    LOG."nome: ${maria.nome}")
    LOG."cpf: ${maria.cpf}")
    LOG."salario: R$${maria.salario}")
    LOG."bonificação: R$${maria.getBonificacao()}")


    //testaComportamentoConta()
    val calculadora = CalculadoraBonificacao()
    calculadora.registra(thiago)
    calculadora.registra(fran)
    calculadora.registra(gui)
    calculadora.registra(maria)

    LOG."total de bonificação: R$${calculadora.total}")
}
