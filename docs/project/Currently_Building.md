# Project Roadmap: Currently Building

This document outlines the development roadmap for the new applications being built with the Python Hypermedia Stack. Each project has a checklist of features and milestones to track its progress.

---

## 1. Text Adventure Game

A complex text-based adventure game with server-side state management and a dynamic, HTMX-driven UI.

### Core Features

- [ ] **Game Engine:** Develop a basic game engine to handle rooms, items, and player state.
- [ ] **Parser:** Implement a simple command parser for player input.
- [ ] **Dynamic Rendering:** Use HTMX to update the game narrative and UI based on player actions.
- [ ] **Database Integration:** Store game state and player progress in a PostgreSQL database.

### Milestones

- [ ] **Phase 1: Basic Prototype:** A simple, playable game with a few rooms and items.
- [ ] **Phase 2: Advanced Features:** Add more complex puzzles, NPCs, and a branching narrative.
- [ ] **Phase 3: Polishing:** Improve the UI, add sound effects, and create a more immersive experience.

---

## 2. Quiz Application

A multiple-choice quiz application with server-side logic for scoring and question management.

### Core Features

- [ ] **Question Bank:** Create a system for managing a bank of quiz questions and answers.
- [ ] **Quiz Logic:** Implement server-side logic for serving questions, tracking scores, and providing results.
- [ ] **Dynamic UI:** Use HTMX for seamless question navigation and real-time feedback.
- [ ] **User Authentication:** Allow users to create accounts and track their quiz history.

### Milestones

- [ ] **Phase 1: Basic Quiz:** A simple quiz with a fixed set of questions.
- [ ] **Phase 2: Advanced Features:** Add different quiz categories, difficulty levels, and a timer.
- [ ] **Phase 3: Polishing:** Improve the UI, add animations, and create a more engaging user experience.

---

## 3. Markdown Editor with Live Preview

A web-based Markdown editor that provides a real-time preview of the rendered HTML.

### Core Features

- [ ] **Markdown Parsing:** Use a Python library to parse Markdown and convert it to HTML.
- [ ] **Live Preview:** Use HTMX to send the Markdown to the server and render the HTML preview in real-time.
- [ ] **File Management:** Allow users to save and load their Markdown files.
- [ ] **Syntax Highlighting:** Add syntax highlighting to the editor and the preview.

### Milestones

- [ ] **Phase 1: Basic Editor:** A simple editor with a live preview.
- [ ] **Phase 2: Advanced Features:** Add support for different Markdown flavors, custom CSS, and a toolbar.
- [ ] **Phase 3: Polishing:** Improve the UI, add themes, and create a more user-friendly experience.

---

## 4. Microblogging Platform

A simplified, Twitter-like platform for posting short messages and interacting with other users.

### Core Features

- [ ] **User Authentication:** Allow users to sign up, log in, and manage their profiles.
- [ ] **Posting:** Implement the ability to create, view, and delete short posts.
- [ ] **Following:** Allow users to follow and unfollow other users.
- [ ] **Timeline:** Create a personalized timeline that shows posts from followed users.
- [ ] **Likes:** Allow users to like and unlike posts.

### Milestones

- [ ] **Phase 1: Basic Platform:** A simple platform with user authentication and posting.
- [ ] **Phase 2: Advanced Features:** Add support for replies, retweets, and direct messages.
- [ ] **Phase 3: Polishing:** Improve the UI, add notifications, and create a more engaging user experience.

---

## 5. System Monitoring Dashboard

A real-time dashboard for monitoring system metrics like CPU, memory, and disk usage.

### Core Features

- [ ] **Metric Collection:** Use a Python library to collect system metrics.
- [ ] **Real-time Updates:** Use HTMX polling or Server-Sent Events (SSE) to update the dashboard in real-time.
- [ ] **Data Visualization:** Use a charting library to create dynamic charts and graphs.
- [ ] **Alerting:** Implement a system for sending alerts when metrics exceed certain thresholds.

### Milestones

- [ ] **Phase 1: Basic Dashboard:** A simple dashboard that displays basic system metrics.
- [ ] **Phase 2: Advanced Features:** Add support for monitoring multiple servers, custom dashboards, and historical data.
- [ ] **Phase 3: Polishing:** Improve the UI, add themes, and create a more user-friendly experience.
