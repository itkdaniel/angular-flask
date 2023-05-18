import { Component } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {
  constructor (private fb: FormBuilder) {}

  loginForm = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required]
  })

  get username() { return this.loginForm.get('username'); }
  get password() { return this.loginForm.get('password'); }
  
  onSubmit () {
    console.log(this.loginForm);
  }
}
