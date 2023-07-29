import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import { Exam } from '../models/exam.mode';
import { environment } from 'src/environments/environment';
import { AuthService } from './auth.service';
const API_BASE_URL = environment.api.base;
// const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
// const requestOptions = { headers: headers };

@Injectable()
export class ExamsApiService {

  constructor(private http: HttpClient, private authService: AuthService) {
  }


  // GET list of public, future events
  getExams(): Observable<any>{
    const httpHeaders: HttpHeaders = new HttpHeaders({
      Authorization: 'Bearer JWT-token'
    });
    const requestOptions = { headers: httpHeaders };
    if (this.authService.isAuthenticated()) {
      const opts = {
        headers: new HttpHeaders({
          Authorization: 'Bearer ' + localStorage.getItem('accessToken')  // tslint:disable-line:object-literal-key-quotes
        })
      };
      return this.http.get<any>(`${API_BASE_URL}/api/exams`, opts);
    }
    return this.http.get<any>(`${API_BASE_URL}/api/exams`,requestOptions);
  }

  // GET an exam
  getExam(id: any): Observable<Exam> {
    return this.http.get<Exam>(`${API_BASE_URL}/api/exam/`+ id); 
  }

  // POST exam details
  addExam(title: any, description: any): Observable<Exam> {
    let exam = new Exam(title, description);
    console.log(`post exam: ${exam}`)
    const httpHeaders: HttpHeaders = new HttpHeaders({
      Authorization: 'Bearer JWT-token'
    });
    const requestOptions = { headers: httpHeaders };
    if (this.authService.isAuthenticated()) {
      const opts = {
        headers: new HttpHeaders({
          Authorization: 'Bearer ' + localStorage.getItem('accessToken')  // tslint:disable-line:object-literal-key-quotes
        })
      };
      return this.http.post<Exam>(`${API_BASE_URL}/api/api/exams`, exam, opts);
    }
    return this.http.post<Exam>(`${API_BASE_URL}/api/apiexams`, exam, requestOptions);
  } 
}

