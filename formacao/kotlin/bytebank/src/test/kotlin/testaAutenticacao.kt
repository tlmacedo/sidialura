import br.com.thiago.bytebank.modelo.Cliente
import br.com.thiago.modelo.Diretor
import br.com.thiago.modelo.Gerente
import br.com.thiago.modelo.SistemaInterno

fun main(){
    testaAutenticacao()
}

fun testaAutenticacao() {
    val gerente = Gerente(
        "Fran",
        "222.222.222-22",
        5000.0,
        2222
    )

    val diretor = Diretor(
        "Thiago",
        "111.111.111-11",
        10000.0,
        1111,
        20.0
    )

    val cliente = Cliente(
        nome = "Gui",
        cpf = "333.333.333-33",
        senha = 1234
    )

    val sistema = SistemaInterno()
    sistema.entra(gerente, 2222)
    sistema.entra(diretor, 1111)
    sistema.entra(cliente, 1234)

}