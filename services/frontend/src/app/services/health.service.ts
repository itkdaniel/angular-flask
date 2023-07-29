import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, map, of, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';
const API_BASE_URL = environment.frontend.base;
const httpHeaders: HttpHeaders = new HttpHeaders({
  Authorization: 'Bearer JWT-token'
});
const requestOptions = { headers: httpHeaders };

export class HealthMessage {
  public ok:string;
  public err:string;
  public constructor() {
    this.ok = "ok  😀";
    this.err = "err  😵";
  }
}  
export class HealthStatus {
  public healthy: boolean;
  public healthMessage: HealthMessage;
  
  public constructor(public health:boolean) {
    this.healthy = health;
    this.healthMessage = new HealthMessage();
  }
  
  isHealthy(): boolean {
    return this.healthy === true;
  }
}
const healthstatus = new HealthStatus(true);

@Injectable({
  providedIn: 'root'
})
export class HealthService {
  health = {status: healthstatus.healthy};
  constructor(private http: HttpClient) { }

  getHealth(): Observable<any> {
    return of(healthstatus);
  }

  checkHealth(): Observable<any> {
    return this.http.get<any>(`${API_BASE_URL}/api/frontend/healthcheck/`, requestOptions)
      .pipe(
        map((response: any) => {
          console.log(`healthcheck response: ${JSON.stringify(response)}`); 
          return response;
        }),
        catchError((e) => {
          console.log('error caught in health service');
          return throwError(() => e);
        })
      );
  }
}
