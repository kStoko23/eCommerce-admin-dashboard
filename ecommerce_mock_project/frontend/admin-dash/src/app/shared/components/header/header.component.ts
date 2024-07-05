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

  // Constructor to subscribe to router events and update active link background on navigation end
  constructor(private router: Router) {
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.updateActiveLinkBackground(event.urlAfterRedirects);
      }
    });
  }

  // Lifecycle hook to set the default active link after view initialization
  ngAfterViewInit(): void {
    this.setDefaultActiveLink();
  }

  // Method to toggle the mobile menu open/close state
  toggleMenu() {
    this.isOpen = !this.isOpen;
  }

  /* Method to set the default active link
   * timeout needed for it to work
   */
  setDefaultActiveLink(): void {
    setTimeout(() => {
      const defaultLink = this.links.first.nativeElement;
      this.updateActiveLink(defaultLink);
    }, 100);
  }

  /* Method to set the active link based on a mouse event
   * (clicking one of the <a></a>)
   */
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

  // Method to update the active link's width and offset, and display the background
  updateActiveLink(linkElement: HTMLElement): void {
    this.activeLinkWidth = `${linkElement.offsetWidth}px`;
    this.activeLinkOffset = `${linkElement.offsetLeft}px`;
    this.displayBackground = true;
  }

  // Method to update the active link background based on the current URL
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
