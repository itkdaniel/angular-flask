import { Component } from '@angular/core';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {
  title = "Home";
  status = {"authenticated": false, "username": null}
  // authenticated: boolean = false;
  // current_user = {"username": null};
  constructor (private fb: FormBuilder, private router: Router, private authService: AuthService) {}

  loginForm = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required]
  })

  get username() { return this.loginForm.get('username'); }
  get password() { return this.loginForm.get('password'); }
  
  onSubmit () {
    this.loginUser();
  }

  private loginUser(): void {
    this.authService.loginUser(this.username?.value, this.password?.value).subscribe(
      res => {
        console.log(JSON.stringify(res));
        if (res["status"] == "success") {
          this.status["authenticated"] = true;
          this.status["username"] = res["user"];
          this.router.navigateByUrl("/exams");
        }
      });
  }

  ngOnInit() {}
}
