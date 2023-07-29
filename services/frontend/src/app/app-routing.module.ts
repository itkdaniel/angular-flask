import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExamListComponent } from './exam-list/exam-list.component';
import { HomePageComponent } from './home-page/home-page.component';
import { AddExamComponent } from './add-exam/add-exam.component';
import { ExamDetailsComponent } from './exam-details/exam-details.component';
import { RegisterComponent } from './register/register.component';
import { ExplorePageComponent } from './explore-page/explore-page.component';
import { ChatComponent } from './chat/chat.component';
import { HealthcheckComponent } from './healthcheck/healthcheck.component';
import { DdsComponent } from './dds/dds.component';

const routes: Routes = [
  { path: '', redirectTo: '/home',pathMatch: 'full' },
  { path: 'home', component: HomePageComponent, title: "AngularFlask-Home"},
  { path: 'exams', component: ExamListComponent, title: "AngularFlask-Exams" },
  { path: 'exam/:id', component: ExamDetailsComponent , title: "AngularFlask-Exam/:id"},
  { path:'add-exam', component: AddExamComponent, title:"AngularFlask-AddExam" },
  { path: 'register', component: RegisterComponent, title: "AngularFlask-Register"},
  { path: 'explore', component: ExplorePageComponent, title: "AngularFlask-Explore"},
  { path: 'chat', component: ChatComponent, title: "AngularFlask-Chat" },
  { path: 'healthcheck', component: HealthcheckComponent, title:"Healthcheck" },
  { path: 'dds', component: DdsComponent, title: "Angular-Flask-DDS" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
