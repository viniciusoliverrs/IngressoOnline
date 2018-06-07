% rebase('view/base.tpl', title='Ver evento')
<div class="row">
        <div class="col-md-12">
               <img class="mx-auto d-block" style="width:500px;height:300px;" src="/Eventos/{{dado[0]}}/banner.jpg" alt="Image not found" />
         	<hr/>
        </div>
    </div>
    <div class="row">
		<div class="col-md-12">
				<table class="table table-striped">
					<tbody>
						<tr>
							<td>Titulo</td>
							<td>{{dado[1]}}</td>
						</tr>
						<tr>
							<td>Categoria</td>
							<td>{{dado[3]}}</td>
						</tr>
						<tr>
							<td>Descrição:</td>
							<td>{{dado[2]}}</td>
						</tr>
						<tr>
							<td>Estado:</td>
							<td>{{dado[9]}}</td>
						</tr>
						<tr>
							<td>Cidade:</td>
							<td>{{dado[8]}}</td>
						</tr>
						<tr>	
							<td>Bairro:</td>
							<td>{{dado[6]}}</td>
						</tr>
						<tr>
							<td>Endereço:</td>
							<td>{{dado[4]}} Nº-{{dado[5]}}</td>
						</tr>
						<tr>
							<td>Telefone:</td>
							<td>{{dado[7]}}</td>
						</tr>
					</tbody>
				</table>
		</div>    	
    </div>
    <div class="row">
		<div class="col-md-12">
			%if len(ingresso) != 0:	
				%include('./view/carrinho/insert.tpl')
			%else:
				<div class="alert alert-info" role="alert">
			  		Nenhum ingresso disponivel.
				</div>
			%end
	</div>
</div>