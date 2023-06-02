import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { Exam } from '../models/exam.mode';
import { ExamsApiService } from '../services/exams-api.service';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-exam-list',
  templateUrl: './exam-list.component.html',
  styleUrls: ['./exam-list.component.css']
})
export class ExamListComponent {
  examsList: Exam[] = [];
  authenticated!: boolean;
  isAdmin: boolean | undefined;
  username: string | undefined;
  message = "";

  constructor(private examsApi: ExamsApiService, private authService: AuthService) {}

  ngOnInit() {
    this.getExams();
    // this.checkUserStatus(history.state["username"]);
    this.authService.subscribe(
      (authenticated) => {
        this.authenticated = authenticated;
        if (authenticated) {
          this.username = this.authService.getUsername();
        } else {
          this.username = undefined;
        }
      }
    );
  }

  getExams() {
    this.examsApi.getExams().subscribe(res => {
      if (res["message"]) {
        this.message = res["message"];
      } else {
        this.examsList = res;
      }
    });
  }

  checkUserStatus(username: any) {
    this.authService.checkUserStatus(username).subscribe(
      res => {
        console.log(`${JSON.stringify(res)}`);
        if (res["status"] == true){
          this.username = res["user"];
          console.log(`status: ${JSON.stringify(res["status"])}`);
          console.log(`current user: ${JSON.stringify(this.username)}`);
        }
      }
    );
  }
}
