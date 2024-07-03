import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
})
export class HeaderComponent {
  ngOnInit() {
    this.addMenuToggleListener();
  }

  addMenuToggleListener() {
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeBtn = document.getElementById('menu-close-btn');

    if (menuBtn && mobileMenu && closeBtn) {
      menuBtn.addEventListener('click', () => {
        mobileMenu.classList.remove('hidden');
      });

      closeBtn.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
      });
    }
  }
}
