'use strict'


class Direction extends React.Component{
	constructor(props) {
		super(props);
		this.state = {
			mathBlockOne: '',
			mathBlockTwo: '',
			phisBlockOne: '',
			phisBlockTwo: '',
			phisBlockThree:'',
			infBlockOne: '',
			infBlockTwo: '',
			socialBlockOne: '',
			socialBlockTwo: '',
			ranking: []
		};


		this.handlerChange = this.handlerChange.bind(this);
		this.handlerSubmit = this.handlerSubmit.bind(this);
	}

	
	handlerChange = (event) =>{
		this.setState({ [event.target.name]: event.target.value});
	}

	handlerSubmit(event){
		event.preventDefault();
		const that = this;
		fetch('http://127.0.0.1:8000/direction/', {
			body: JSON.stringify(this.state),
			headers: {
				'content-type': 'application/json'
			},
			method: 'POST',
		})
		.then(function (response) {
			console.log(response);
			if (response.status === 200) {
				return response.json();
				
			} else {
				alert('Ошибка отправки данных!');
			}
		})
		.then(function(results) { 
			that.setState({
				mathBlockOne: '',
				mathBlockTwo: '',
				phisBlockOne: '',
				phisBlockTwo: '',
				phisBlockThree:'',
				infBlockOne: '',
				infBlockTwo: '',
				socialBlockOne: '',
				socialBlockTwo: '',
				ranking: results["result"]
			});
		});
	}


	render() {
		const { mathBlockOne, mathBlockTwo, phisBlockOne, phisBlockTwo, 
			phisBlockThree, infBlockOne, infBlockTwo, socialBlockOne, 
			socialBlockTwo, ranking } = this.state;
		return(
			<div>
				<label className = "title">Расставьте приоритеты для каждого блока дисциплин</label>
				<div className="directions">
					<div>Блоки изучаемых дисциплин </div> <div >минимум</div> <div>не имеет значения</div>  <div >максимум</div>
				   		<p className='blockName'>Фундаментальная математика:</p><input type="radio" name = 'mathBlockOne' value = {'min'} onClick = {this.handlerChange}></input><input type="radio" ></input><input type="radio" name = 'mathBlockOne' value = {'max'} onClick = {this.handlerChange}></input> 
				    	<p className='blockName'>Специальная математика:</p><input type="radio" name = 'mathBlockTwo' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'mathBlockTwo' value = {'max'} onClick = {this.handlerChange}></input>
				   	 	<p className='blockName'>Конструирование и инженерное дело:</p><input type="radio" name = 'phisBlockOne' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'phisBlockOne' value = {'max'}></input>
				    	<p className='blockName'>Техническая физика:</p><input type="radio" name = 'phisBlockTwo' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'phisBlockTwo' value = {'max'} onClick = {this.handlerChange}></input>
				   		<p className='blockName'>Общая физика:</p><input type="radio" name = 'phisBlockThree' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'phisBlockThree' value = {'max'} onClick = {this.handlerChange}></input>
				    	<p className='blockName'>Математическая информатика:</p><input type="radio" name = 'infBlockOne' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'infBlockOne' value = {'max'} onClick = {this.handlerChange}></input> 
				    	<p className='blockName'>Прикладная информатика:</p><input type="radio" name = 'infBlockTwo' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'infBlockTwo' value = {'max'} onClick = {this.handlerChange}></input>
				    	<p className='blockName'>Лингвистика:</p><input type="radio" name = 'socialBlockOne' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'socialBlockOne' value = {'max'} onClick = {this.handlerChange}></input>
				    	<p className='blockName'>Экономика и менеджмент:</p><input type="radio" name = 'socialBlockTwo' value = {'min'} onClick = {this.handlerChange}></input><input type="radio"></input><input type="radio" name = 'socialBlockTwo' value = {'max'} onClick = {this.handlerChange}></input>
					</div>

		    <button className="buttonGet" onClick = {this.handlerSubmit}>Узнать результаты!</button>
			    			<label className = "title">Вы можете рассмотреть следующие меганаправления:</label>

			    			<div className = 'results'> 
			    			<div><span id = 'span'>1</span><span id = 'spna'><a href = "https://priem.mai.ru/mega/">{ranking[0]}</a></span></div> 
			    			<div><span id = 'span'>2</span><span id = 'spna'><a href = "https://priem.mai.ru/mega/">{ranking[1]}</a></span></div>
			    			<div><span id = 'span'>3</span><span id = 'spna'><a href = "https://priem.mai.ru/mega/">{ranking[2]}</a></span></div>
			    			</div>



		</div>	
		);
	}
}

ReactDOM.render(<Direction />, document.getElementById('direction'));
