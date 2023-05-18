import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExamListComponent } from './exam-list/exam-list.component';
import { HomePageComponent } from './home-page/home-page.component';
import { AddExamComponent } from './add-exam/add-exam.component';

const routes: Routes = [
  { path: '', redirectTo: '/home',pathMatch: 'full' },
  { path: 'home', component: HomePageComponent },
  { path: 'exams', component: ExamListComponent },
  { path:'add-exam', component: AddExamComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
