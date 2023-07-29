import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { TextResponse } from '../models/textresponse.mode';
import { Observable, catchError, map, of, throwError } from 'rxjs';
const API_BASE_URL = environment.api.base;
const endpoints = {chat:'api/gpt/genchat',ping: 'api/gpt/ping'}
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
          console.error(`error caught in chatgen service: ${e}`);
          let errResponse = {"sno":1,"role":"assistant","text":`${data.text}`,"response":"<blockquote>This is an <code>🤓 😎<strong><i>automatic response 🥶</i></strong></code> as an <b>artificially intelligent <code><i>AGI 🤖</i></code></b> (<p><small><i>Artificial General Intelligence 👽</i></small></p>). Please <small style='cursor: pointer;'><kbd><kbd>➢</kbd>connect</kbd></small> to the 💩 👻 API <u>  🎃 😺 ( <a href='#'>application programming interface</a> )</u> to test for a <mark>real response</mark>. Have a good day <footer class='blockquote-footer'>AI Model <cite title='gpt-3.5-turbo'>gpt-3.5-turbo🤑 😄 😁 😆😮‍💨</cite></footer></blockquote>"}
          return of(errResponse);
        })
      );
  }
}
