package br.com.thiago.modelo

import br.com.thiago.bytebank.modelo.Cliente
import br.com.thiago.bytebank.modelo.Conta
import br.com.thiago.bytebank.modelo.isTransferencia

class ContaCorrente(
    titular: Cliente,
    numero: Int
) : Conta(
    titular = titular,
    numero = numero
) {

    override fun saca(valor: Double): Boolean {
        val valorComTaxa = valor + 0.1
        if (!validaValor(valorComTaxa)) return false
        if (saldo >= valorComTaxa) {
            saldo -= valorComTaxa
            if (!isTransferencia) {
                LOG."Sacando R$$valorComTaxa na conta do $titular.")
                imprimeSaldo()
            }
            return true
        } else {
            if (!isTransferencia)
                LOG."Saldo R$ $saldo, é insuficiente para sacar R$ $valorComTaxa na conta de $titular.")
        }
        return false
    }

}