package br.com.thiago.bytebank.modelo

class ContaPoupanca(
    titular: Cliente,
    numero: Int
) : Conta(
    titular = titular,
    numero = numero
) {
    override fun saca(valor: Double): Boolean {
        if (!this.validaValor(valor)) return false
        if (saldo >= valor) {
            saldo -= valor
            if (!isTransferencia) {
                LOG."Sacando R$$valor na conta do $titular")
                imprimeSaldo()
            }
        } else {
            if (!isTransferencia)
                LOG."Saldo R$$saldo, é insuficiente para sacar R$ $valor")
        }
        return false

    }


}