import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { User } from '../models/user.mode';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  constructor (private fb: FormBuilder, private router: Router, private auth: AuthService) {}

  registerForm = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required]
  });

  get username() {return this.registerForm.get('username')};
  get password() {return this.registerForm.get('password')};

  new_user: User | undefined;

  onSubmit() {
    if (this.registerForm.invalid) {
      alert('Please complete register form')
    } else {
      this.auth.registerUser(this.username?.value, this.password?.value).subscribe(data => {
        this.new_user = data['user'];
        console.log(`new_user username: ${this.new_user?.username}`)
        console.log(JSON.stringify(data['user']));
        if (data['status'] == 'success'){
          this.router.navigateByUrl("/home")
        }
      })
    }
  }
}
