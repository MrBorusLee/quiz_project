import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

let apiURL = 'http://127.0.0.1:8000/api/';


class App extends Component {
  constructor(){
    super();
    this.state = {question: '', answers: []};
    this.qa_list = [];
  }

  saveData(response){
    this.setState({question: response.data, answers: response.data.answers});
  }

  componentWillMount(){
    axios.get(`${apiURL}questions/first/`).then(response => {
      this.saveData(response)
    })
  }

  answerQuestion(answer){
    this.qa_list.push({question_id: this.state.question.id, answer_id: answer.id});
    axios.get(`${apiURL}questions/${answer.next_question}/`).then(response => {
      this.saveData(response);
      if (response.data.answers.length === 0){
        axios.post(`${apiURL}questions/finish_quiz/`, this.qa_list)
      }
    })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>{this.state.question.question}</h1>
          {
            this.state.answers.map(answer => <p key={answer.id} onClick={this.answerQuestion.bind(this, answer)}>{answer.answer}</p>)
          }
        </header>
      </div>
    );
  }
}

export default App;
