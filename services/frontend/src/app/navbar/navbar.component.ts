import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  authenticated!: boolean;
  username: string | undefined;

  constructor (private authService: AuthService) {}
  
  ngOnInit() {
    this.authService.subscribe(
      (authenticated) => {
        this.authenticated = false;
        if (authenticated) {
          this.username = this.authService.getUsername();
        } else {
          this.username = undefined;
        }
      }
    );
  }
}
