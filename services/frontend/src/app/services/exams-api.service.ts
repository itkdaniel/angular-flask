import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import { Exam } from '../models/exam.mode';
import { environment } from 'src/environments/environment';
const API_BASE_URL = environment.api.base;

@Injectable()
export class ExamsApiService {

  constructor(private http: HttpClient) {
  }


  // GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http
      .get<Exam[]>(`${API_BASE_URL}/exams`);
  }
}

