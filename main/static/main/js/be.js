'use strict'


class Form extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			name: '',
			school: '',
			email: '',
			classNumber: '10',
			town:'',
			phoneNumber: ''
		};


		this.handlerChange = this.handlerChange.bind(this);
		this.handlerSubmit = this.handlerSubmit.bind(this);
	}

	handlerChange = (event) =>{
		this.setState({ [event.target.name]: event.target.value});
	}

	handlerSubmit(event){
		event.preventDefault();
		fetch('https://phmschool.herokuapp.com/enter/', {
			body: JSON.stringify(this.state),
			headers: {
				'content-type': 'application/json'
			},
			method: 'POST',
		})
		.then(function (response) {
			if (response.status === 200) {
				alert('Данные успешно отправлены!');
			} else {
				alert('Ошибка отправки данных!');
			}
		});

		this.setState({name: '',
						phoneNumber: '',
						school: '',
						email: '',
						town: '',
						classNumber: ''
					});
	}


	render() {
		const { name, phoneNumber, school, email, town, classNumber } = this.state;
		return(
			<form onSubmit={this.handlerSubmit} method = "POST">
		 		<input id='drt' type="text" name = 'name'  value = {name}
		 			   onChange={this.handlerChange} className="name"
		 			   placeholder="Фамилия Имя Отчество" maxLength="130">
		 		</input> <br />
		 		<input id='drt' type="email" name = 'email' value = {email}
		 			onChange={this.handlerChange} className="email"
		 			placeholder="example@mail.ru">
		 		</input><br />
		 		<input   id='drt' type="tel" name = "phoneNumber" value = {phoneNumber}
		 			onChange={this.handlerChange} className="phoneNumber"
		 			placeholder="+7-000-000-0000" pattern="+7-9[0-9]{2}-[0-9]{3}-[0-9]{4}" maxLength="11">
		 		</input><br />
		 		<input id='drt' type="text" className="school" name = "school"  value = {school}
		 			onChange={this.handlerChange} placeholder = "Школа">
		 		</input><br />
		    	<input id='drt'type="text"  className="town" name = "town" value = {town}
		    		placeholder = "Город"  onChange={this.handlerChange}>
		    	</input><br />
		    	<label id='qwerty'> Класс поступления: &nbsp; &nbsp; &nbsp;</label>
		    	<select name = 'classNumber' className = 'classNumber' onChange = {this.handlerChange}
		    		value = {classNumber}>
		    		<option value = {10} id = "num">10</option>
		    		<option value = {11} id = "num">11</option>
		    	</select>
		    	<br /> <br />
		    	<button className="button" >Отправить</button>
		    </form>

		);
	}
}


ReactDOM.render(<Form />, document.getElementById('form'));
