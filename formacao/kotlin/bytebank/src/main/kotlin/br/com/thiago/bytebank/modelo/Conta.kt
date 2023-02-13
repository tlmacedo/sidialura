package br.com.thiago.bytebank.modelo

var isTransferencia : Boolean = false
var totalContas = 0
    private set

abstract class Conta(
    var titular: Cliente,
    val numero: Int
) {

    var saldo = 0.0
        protected set

    init {
        totalContas++
        println("Criando conta")
    }

    fun imprimeSaldo() {
        println("Saldo atualizada do(a) ${titular.nome} é de R$ $saldo")
    }

    fun deposita(valor: Double) {
        if (!validaValor(valor)) return
        if (!isTransferencia)
            println("Depositando R$ $valor na conta do ${titular.nome}.")
        saldo += valor
        imprimeSaldo()
    }

    abstract fun saca(valor: Double): Boolean

    fun transfere(valor: Double, destino: Conta) {
        isTransferencia = true
        if (!validaValor(valor)) return
        println("Transferindo R$ $valor de: $titular para: ${destino.titular}")

        if (saca(valor)) {
            destino.deposita(valor)
            imprimeSaldo()
        }
        isTransferencia = false
    }

    fun validaValor(valor: Double): Boolean {
        return (valor > 0.0)
    }

//    fun getTitular(): String {
//        return titular
//    }
//
//    fun setTitular(nome: String) {
//        if (nome.isEmpty() || nome.equals("")) return
//        titular = nome
//    }
//
//    fun getNumero(): Int {
//        return numero
//    }
//
//    fun setNumero(num: Int) {
//        if (num <= 0) return
//        numero = num
//    }
//
//    fun getSaldo(): Double {
//        return saldo
//    }
//
//    fun setSaldo(valor: Double) {
//        saldo = valor
//    }

}