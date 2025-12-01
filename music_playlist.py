import random
from abc import ABC, abstractmethod
from typing import List, Tuple
from datetime import datetime

#.........Parent class of Song............
class Song(ABC):
    
    def __init__(self, name: str, artist: str, length: int):  # Constructor store song info as tuple
        self._info: Tuple[str, str, int] = (name, artist, length)
    @property
    def info(self) -> Tuple[str, str, int]:    #Geting song information as tuple (name, artist, length)  
        return self._info
    
    @property
    def name(self) -> str:
        return self._info[0]
    
    @property
    def artist(self) -> str:
        return self._info[1]
    
    @property
    def length(self) -> int:
        return self._info[2]
    
    def format_length(self) -> str:             #Format length as MM:SS
        mins = self.length // 60
        secs = self.length % 60
        return f"{mins}:{secs:02d}"
    
    @abstractmethod
    def play(self) -> str:    #Play the song - to be implemented by subclasses
        pass
    def __str__(self) -> str:
        return f"{self.name} by {self.artist} [{self.format_length()}]"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.artist}, {self.length})"

class LocalSong(Song):   # Represents a locally stored song
    def __init__(self, name: str, artist: str, length: int, file_path: str):
        super().__init__(name, artist, length)
        self.file_path = file_path
    
    def play(self) -> str:           #   Play local song

        return (f"🎵 Playing from local file: {self.file_path}\n   {self}")
class OnlineSong(Song):
    """Represents an online streaming song"""
    
    def __init__(self, name: str, artist: str, length: int, url: str):
        super().__init__(name, artist, length)
        self.url = url
    
    def play(self) -> str:
        """Stream online song"""
        return f"Streaming from: {self.url}\n   {self}"


class Playlist:     #  Manages a music playlist
    def __init__(self, name: str):
        self.name = name
        self._songs: List[Song] = []
        self._recently_played: List[Tuple[Song, str]] = []
        self._max_recent = 10
    
    def add_song(self, song: Song) -> None:     # Add a song to the playlist

        self._songs.append(song)
        print(f"✓ Added: {song}")
    
    def remove_song(self, song_name: str) -> bool:

        for i, song in enumerate(self._songs):
            if song.name.lower() == song_name.lower():
                removed = self._songs.pop(i)
                print(f"✓ Removed: {removed}")
                return True
        print(f"✗ Song '{song_name}' not found")
        return False
    
    def shuffle(self) -> None:
        """Shuffle the playlist"""
        random.shuffle(self._songs)
        print("🔀 Playlist shuffled!")
    
    def play_song(self, index: int) -> None:
        """Play a song at given index"""
        if 0 <= index < len(self._songs):
            song = self._songs[index]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Polymorphism in action - same method, different behavior
            print(song.play())
            
            # Add to recently played
            self._recently_played.append((song, timestamp))
            if len(self._recently_played) > self._max_recent:
                self._recently_played.pop(0)
        else:
            print(" Invalid song index")
    
    def play_next(self) -> None:
        """Play the first song in playlist"""
        if self._songs:
            self.play_song(0)
        else:
            print("✗ Playlist is empty")
    
    def display_playlist(self) -> None:
        """Display all songs in playlist"""
        if not self._songs:
            print(f"\nPlaylist '{self.name}' is empty")
            return
        
        print(f"\nPlaylist: {self.name}")
        print("=" * 60)
        for i, song in enumerate(self._songs, 1):
            song_type = "🎵" if isinstance(song, LocalSong) else "🌐"
            print(f"{i}. {song_type} {song}")
    
    def display_recently_played(self) -> None:
        """Display recently played songs"""
        if not self._recently_played:
            print("\n⏱ No recently played songs")
            return
        
        print(f"\n Recently Played (Last {len(self._recently_played)})")
        print("=" * 60)
        for song, timestamp in reversed(self._recently_played):
            song_type = "local" if isinstance(song, LocalSong) else "remote"
            print(f"{song_type} {song}")
            print(f"   Played at: {timestamp}")
    
    def get_total_length(self) -> Tuple[int, str]:
        """Get total playlist length"""
        total_secs = sum(song.length for song in self._songs)
        hours = total_secs // 3600
        mins = (total_secs % 3600) // 60
        secs = total_secs % 60 
        formatted = f"{hours}h {mins}m {secs}s" if hours else f"{mins}m {secs}s"
        return total_secs, formatted
    def __len__(self) -> int:
        return len(self._songs)
    def __str__(self) -> str:
        _, length = self.get_total_length()
        return f"Playlist '{self.name}' - {len(self)} songs, {length}"


def display_menu() -> None:
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("MUSIC PLAYLIST APP")
    print("=" * 60)
    print("1. Add Local Song")
    print("2. Add Online Song")
    print("3. Remove Song")
    print("4. Display Playlist")
    print("5. Shuffle Playlist")
    print("6. Play Next Song")
    print("7. Play Song by Number")
    print("8. Show Recently Played")
    print("9. Playlist Info")
    print("0. Exit")
    print("=" * 60)
    
def main():
    """Main application loop"""
    playlist = Playlist("My Awesome Playlist")
    
    # Add some sample songs
    playlist.add_song(LocalSong("Bohemian Rhapsody", "Queen", 354, "/music/queen_br.mp3"))
    playlist.add_song(OnlineSong("Shape of You", "Ed Sheeran", 234, "https://spotify.com/shape-of-you"))
    playlist.add_song(LocalSong("Imagine", "John Lennon", 183, "/music/imagine.mp3"))
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            name = input("Song name: ")
            artist = input("Artist: ")
            try:
                length = int(input("Length (seconds): "))
                file_path = input("File path: ")
                song = LocalSong(name, artist, length, file_path)
                playlist.add_song(song)
            except ValueError:
                print("✗ Invalid length")
        
        elif choice == "2":
            name = input("Song name: ")
            artist = input("Artist: ")
            try:
                length = int(input("Length (seconds): "))
                url = input("URL: ")
                song = OnlineSong(name, artist, length, url)
                playlist.add_song(song)
            except ValueError:
                print("✗ Invalid length")
        
        elif choice == "3":
            song_name = input("Enter song name to remove: ")
            playlist.remove_song(song_name)
        
        elif choice == "4":
            playlist.display_playlist()
        
        elif choice == "5":
            playlist.shuffle()
        
        elif choice == "6":
            playlist.play_next()
        
        elif choice == "7":
            try:
                index = int(input("Enter song number: ")) - 1
                playlist.play_song(index)
            except ValueError:
                print("✗ Invalid number")
        
        elif choice == "8":
            playlist.display_recently_played()
        
        elif choice == "9":
            print(f"\n {playlist}")
        
        elif choice == "0":
            print("\nThanks for using Music Playlist App!")
            break
        
        else:
            print("✗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()