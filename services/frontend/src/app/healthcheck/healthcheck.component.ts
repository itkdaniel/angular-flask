import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HealthService, HealthStatus } from '../services/health.service';
// export class HealthMessage {
//   public ok:string;
//   public err:string;
//   public constructor() {
//     this.ok = "ok  😀";
//     this.err = "err  😵";
//   }
// }  
// export class HealthStatus {
//   public healthy: boolean;
//   public healthMessage: HealthMessage;
  
//   public constructor(public health:boolean) {
//     this.healthy = health;
//     this.healthMessage = new HealthMessage();
//   }

//   isHealthy(): boolean {
//     return this.healthy === true;
//   }
// }

@Component({
  selector: 'app-healthcheck',
  templateUrl: './healthcheck.component.html',
  styleUrls: ['./healthcheck.component.css']
})



export class HealthcheckComponent {
  public healthstatus!: HealthStatus;
  status!: string;
  message!:string;
  constructor (private healthService:HealthService,private router: Router) {}

  ngOnInit () {
    this.isHealthy();
    this.checkHealth();
    // console.log(`healthstatus: ${this.healthstatus.healthy}`);
    // console.log(`healthmessage: ${this.healthstatus.healthMessage}`);
  }

  isHealthy(): boolean {
    this.healthService.getHealth().subscribe( (resp) => {
      console.log(`healthstatus: ${resp.healthy}`);
      console.log(`healthmessage: ${resp.healthMessage}`);
      this.healthstatus = resp;
    });
    return this.healthstatus.healthy;
  }

  checkHealth(): any {
    this.healthService.checkHealth().subscribe( (resp) => {
      console.log(`response: ${resp}`);
      console.log(`healthstatusapi: ${resp.healthstatus}`);
      console.log(`message: ${resp.message}`);
      this.status = resp.healthstatus;
      this.message = resp.message;
    });
  }
  
}
