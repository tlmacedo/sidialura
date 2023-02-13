package br.com.thiago.bytebank

import br.com.thiago.bytebank.modelo.Cliente
import mu.KotlinLogging

var LOG = KotlinLogging.logger { }

fun main() {

    val palavra = "Kotlin"

    val cliente = Cliente(nome = "Thiago", cpf =  "11111111", senha =  1)

}


