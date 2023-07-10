import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { TextResponse } from '../models/textresponse.mode';
import { Observable, catchError, map, throwError } from 'rxjs';
const API_BASE_URL = environment.api.base;
const endpoints = {chat:'gpt/genchat',ping: 'gpt/ping'}
const httpHeaders: HttpHeaders = new HttpHeaders({
  'Content-Type': 'application/json',
  Authorization: 'Bearer BetterChatGPT'
});
const requestOptions = { headers: httpHeaders };
@Injectable({
  providedIn: 'root'
})
export class ChatgenService {

  constructor(private http: HttpClient) { }

  pingpong(data:TextResponse): Observable<any> {
    return this.http.post<any>(`${API_BASE_URL}/${endpoints.ping}`,data,requestOptions)
      .pipe(
        map((response:any) => {
          return response;
        }),
        catchError((e) => {
          console.error(`error caught in ping endpoint`);
          return throwError(() => e);
        })
      );
  }

  genchat(data:TextResponse): Observable<any> {
    // throw new Error("Mehtod not implemented")
    return this.http.post<any>(`${API_BASE_URL}/${endpoints.chat}`,data,requestOptions)
      .pipe(
        map((response:any) => {
          return response;
        }),
        catchError((e) => {
          console.error(`error caught in chatgen service`);
          return throwError(() => e);
        })
      );
  }
}
