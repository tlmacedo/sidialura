package br.com.tlmacedo.agenda.ui.activity

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity
import br.com.tlmacedo.agenda.R
import br.com.tlmacedo.agenda.dao.AlunoDAO
import br.com.tlmacedo.agenda.model.Aluno

private const val TITULO_APPBAR = "Novo aluno"
private val dao: AlunoDAO = AlunoDAO()

class FormularioAlunoActivity : AppCompatActivity() {

    private var campoNome: EditText? = null
    private var campoTelefone: EditText? = null
    private var campoEmail: EditText? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_formulario_aluno)
        setTitle(TITULO_APPBAR)
        inicializacaoDosCampos()
        configuraBotaoSalvar()
        configuraBotaoSalvar()
    }

    private fun inicializacaoDosCampos() {
        campoNome = findViewById<EditText>(R.id.activity_formulario_aluno_nome)
        campoTelefone = findViewById<EditText>(R.id.activity_formulario_aluno_telefone)
        campoEmail = findViewById<EditText>(R.id.activity_formulario_aluno_email)

    }

    private fun configuraBotaoSalvar() {
        val botaoSalvar = findViewById<Button>(R.id.activity_formulario_aluno_botao_salvar)
        botaoSalvar.setOnClickListener {
            val alunoCriado = criaAluno()
            salva(alunoCriado)
        }
    }

    private fun salva(aluno: Aluno) {
        dao.salva(aluno)
        finish()
    }

    private fun criaAluno(): Aluno {
        val nome: String = campoNome?.getText().toString()
        val telefone = campoTelefone?.getText().toString()
        val email = campoEmail?.getText().toString()

        return Aluno(nome, telefone, email)
    }

}