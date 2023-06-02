import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ExamListComponent } from './exam-list/exam-list.component';
import { HttpClientModule } from '@angular/common/http';
import { ExamsApiService } from './services/exams-api.service';
import { HomePageComponent } from './home-page/home-page.component';
import { AddExamComponent } from './add-exam/add-exam.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ExamDetailsComponent } from './exam-details/exam-details.component';
import { RegisterComponent } from './register/register.component';

@NgModule({
  declarations: [
    AppComponent,
    ExamListComponent,
    HomePageComponent,
    AddExamComponent,
    NavbarComponent,
    ExamDetailsComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [ExamsApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
