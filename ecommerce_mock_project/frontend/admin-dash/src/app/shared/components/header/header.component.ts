import { Component, ElementRef, QueryList, ViewChildren } from '@angular/core';
import {
  NavigationEnd,
  Router,
  RouterLink,
  RouterLinkActive,
  RouterOutlet,
} from '@angular/router';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive, CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
})
export class HeaderComponent {
  @ViewChildren('links', { read: ElementRef }) links: QueryList<ElementRef>;

  isOpen = false;
  activeLinkWidth: string;
  activeLinkOffset: string;
  displayBackground: boolean = true;

  constructor(private router: Router) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.updateActiveLinkBackground(event.urlAfterRedirects);
      }
    });
  }

  ngAfterViewInit(): void {
    this.setDefaultActiveLink();
  }

  toggleMenu() {
    this.isOpen = !this.isOpen;
  }

  setDefaultActiveLink(): void {
    setTimeout(() => {
      const defaultLink = this.links.first.nativeElement;
      this.updateActiveLink(defaultLink);
    }, 50);
  }

  setActiveLink(event: MouseEvent): void {
    const target = event.target as HTMLElement;
    const linkElement = target.closest('.link');

    if (!linkElement) return;

    const linkArray = this.links.toArray();
    var index = linkArray.findIndex((el) => el.nativeElement === linkElement);

    if (index === -1) return;

    const link = linkArray[index].nativeElement;

    this.updateActiveLink(link);
  }

  updateActiveLink(linkElement: HTMLElement): void {
    this.activeLinkWidth = `${linkElement.offsetWidth}px`;
    this.activeLinkOffset = `${linkElement.offsetLeft}px`;
    this.displayBackground = true;
  }
  updateActiveLinkBackground(url: string): void {
    const activeLinks = this.links.filter(
      (link) => link.nativeElement.getAttribute('routerLink') === url
    );
    if (activeLinks.length > 0) {
      this.updateActiveLink(activeLinks[0].nativeElement);
    } else {
      this.displayBackground = false;
    }
  }
}
