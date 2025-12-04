# Music_playlist App
A simple Python music playlist manager demonstrating **Classes, Inheritance, Polymorphism, and Abstract Classes**.

# Features
| Feature |	Description |
| --- | --- |
| Add Songs |	Add local or online songs |
| Remove Songs |	Remove by song name |
| Shuffle |	Randomize playlist order |
| Play Songs |	Play by number or next |
|Recently Played |	Track last 10 played songs |
| Playlist Info |	View total songs and duration |

# Menu Options
1. Add Local Song
2. Add Online Song
3. Remove Song
4. Display Playlist
5. Shuffle Playlist
6. Play Next Song
7. Play Song by Number
8. Show Recently Played
9. Playlist Info
0. Exit

# Create playlist
playlist = Playlist("My Playlist")

# Add local song
song1 = LocalSong("Imagine", "John Lennon", 183, "/music/imagine.mp3")
playlist.add_song(song1)

# Add online song
song2 = OnlineSong("Shape of You", "Ed Sheeran", 234, "https://spotify.com/shape")
playlist.add_song(song2)

# Play song (Polymorphism)
song1.play()  # 🎵 Playing from local file: /music/imagine.mp3
song2.play()  # 🌐 Streaming from: https://spotify.com/shape

# Shuffle and play
playlist.shuffle()
playlist.play_next()

# OOP Concepts
| Concept |	Example |
| --- | --- |
| Abstract Class |	Song(ABC) with @abstractmethod play() |
| Inheritance	| LocalSong(Song), OnlineSong(Song) |
| Polymorphism |	play() works differently for each song type |
| Encapsulation	| Private _songs, _recently_played |
| Tuple | Storage	Song info stored as (name, artist, length) |

#  Class Diagram
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/dcb9dfef-6e43-4e9b-83a5-00f3bd2d4bd9" />

#  Song Types
| Type |	Storage |	Play Method |
| --- | --- |
| LocalSong |	File | path	Plays from local file |
| OnlineSong |	URL	| Streams from internet |

# Sample Output
<img width="1335" height="576" alt="image" src="https://github.com/user-attachments/assets/95c1f7ba-bd3a-417a-8029-16d8526a6ca3" />




