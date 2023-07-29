import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { Observable } from 'rxjs/internal/Observable';
import { environment } from 'src/environments/environment';
import { User } from '../models/user.mode';
import { catchError } from 'rxjs/internal/operators/catchError';
import { throwError } from 'rxjs/internal/observable/throwError';
import { map, BehaviorSubject } from 'rxjs';
const API_BASE_URL = environment.api.base;
const httpHeaders: HttpHeaders = new HttpHeaders({
  Authorization: 'Bearer JWT-token'
});
const requestOptions = { headers: httpHeaders };

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private jwt: JwtHelperService = new JwtHelperService();
  private authStatus: BehaviorSubject<boolean> = new BehaviorSubject(this.isAuthenticated());

  constructor(private http: HttpClient) { }

  subscribe(next: (status: boolean) => void) {
    this.authStatus.subscribe(next);
  }

  checkUserStatus(username: any): Observable<any> {
    const opts = {
      headers: new HttpHeaders({
        Authorization: 'Bearer ' + localStorage.getItem('accessToken')  // tslint:disable-line:object-literal-key-quotes
      })
    };
    return this.http.post<any>(`${API_BASE_URL}/api/users/status`, {"username": username}, opts)
      .pipe(
        map(response => {
          console.log(`status response: ${JSON.stringify(response)}`);
          return response;
        })
      );
  }

  loginUser(username: any, password: any): Observable<any> {
    let user = new User(username,password);
    return this.http.post<any>(`${API_BASE_URL}/api/users/login`, user, requestOptions)
      .pipe(
        map(response => {
          // console.log(`auth service access token: ${response["access_token"]}`)
          // console.log(`auth service refresh token: ${response["refresh_token"]}`)
          localStorage.setItem('accessToken', response["access_token"]);
          localStorage.setItem('refreshToken', response["refresh_token"]);
          localStorage.setItem('username', response["user"]);
          this.authStatus.next(true);
          return response;
        }));
  }

  registerUser(username: any, password: any): Observable<any> {
    let user = new User(username,password);
    return this.http.post<any>(`${API_BASE_URL}/api/users/register`, user, requestOptions)
      .pipe(
        catchError((e) => {
          console.log('error caught in register service');
          return throwError(() => e);
        })
      );
  }

    // User is logged in
    isAuthenticated(): any {
      return localStorage.getItem('username') !== null &&
             !this.jwt.isTokenExpired(localStorage.getItem('refreshToken'));
    }
  
    // User is an administrator
    isAdmin(): any {
      return localStorage.getItem('isAdmin') === 'true';
    }
  
    // get username
    getUsername(): any {
      return localStorage.getItem('username');
    }
}
