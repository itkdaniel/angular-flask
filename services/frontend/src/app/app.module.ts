import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ExamListComponent } from './exam-list/exam-list.component';
import { HttpClientModule } from '@angular/common/http';
import { ExamsApiService } from './services/exams-api.service';

@NgModule({
  declarations: [
    AppComponent,
    ExamListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [ExamsApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
