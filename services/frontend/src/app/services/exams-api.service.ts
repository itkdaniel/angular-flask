import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import { Exam } from '../models/exam.mode';
import { environment } from 'src/environments/environment';
const API_BASE_URL = environment.api.base;
// const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
// const requestOptions = { headers: headers };

@Injectable()
export class ExamsApiService {

  constructor(private http: HttpClient) {
  }


  // GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http.get<Exam[]>(`${API_BASE_URL}/exams`);
  }

  // GET an exam
  getExam(id: any): Observable<Exam> {
    return this.http.get<Exam>(`${API_BASE_URL}/exam/`+ id); 
  }

  // POST exam details
  addExam(title: any, description: any): Observable<Exam> {
    let exam = new Exam(title, description);
    console.log(`post exam: ${exam}`)
    const httpHeaders: HttpHeaders = new HttpHeaders({
      Authorization: 'Bearer JWT-token'
  });
    const requestOptions = { headers: httpHeaders };
    return this.http.post<Exam>(`${API_BASE_URL}/exams`, exam, requestOptions);
  } 
}

