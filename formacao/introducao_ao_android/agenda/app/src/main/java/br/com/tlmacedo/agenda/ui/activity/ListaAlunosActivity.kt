package br.com.tlmacedo.agenda.ui.activity

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.ArrayAdapter
import android.widget.ListView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import br.com.tlmacedo.agenda.R
import br.com.tlmacedo.agenda.dao.AlunoDAO
import br.com.tlmacedo.agenda.model.Aluno
import com.google.android.material.floatingactionbutton.FloatingActionButton


private const val TITULO_APPBAR = "Lista de alunos."
private val dao = AlunoDAO()

class ListaAlunosActivity() : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_lista_alunos)
        setTitle(TITULO_APPBAR)
        configurarFabNovoAluno()
        dao.salva(Aluno("Thiago", "12345", "thiago.macedo"))
        dao.salva(Aluno("Carla", "54321", "carla.macedo"))
    }

    private fun configurarFabNovoAluno() {
        val botaoNovoAluno = findViewById<FloatingActionButton>(R.id.lista_alunos_fab_novo_aluno)
        botaoNovoAluno.setOnClickListener {
            abrerFormularioAlunoActivity()
        }
    }

    private fun abrerFormularioAlunoActivity() {
        startActivity(Intent(this, FormularioAlunoActivity::class.java))
    }

    override fun onResume() {
        super.onResume()
        configuraLista()

    }

    private fun configuraLista() {
        val listaDeAlunos = findViewById<ListView>(R.id.activity_lista_alunos_listview)
        listaDeAlunos.adapter = ArrayAdapter<Any?>(
            this,
            android.R.layout.simple_list_item_1,
            dao.todos() as List<Any?>
        )
        listaDeAlunos.setOnItemClickListener { adapterView, view, posicao, id ->
            Log.i("posicao aluno", "" + posicao)
        }
    }

}