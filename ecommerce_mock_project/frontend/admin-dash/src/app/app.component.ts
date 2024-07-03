import { Component } from '@angular/core';
import { RouterLinkActive, RouterOutlet } from '@angular/router';
import { HeaderComponent } from './shared/components/header/header.component';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, RouterLink, RouterLinkActive],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'admin-dash';
}
