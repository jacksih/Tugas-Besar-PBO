import pygame


class space_invaders:
    def __init__(self) -> None:
        self.score = 0
        self.lives = 3
        # self.player =
        # self.enemy
        # self.font = # buat font score dan result
        # self.enemy_laser # untuk enemy laser
        # self.music
        # self.laser_sound
        # self.eksplosion_sound # ledakan jika laser mengenai player atau enemy

    def collision(self):
        """
        algoritma jika laser enemy mengenai player, laser player mengenai enemy, 
        laser enemy tidak mengenai player, juga nilai score ketika pemain berhasil membunuh enemy
        """
        pass

    def enemy_setup(self):
        """algoritma penambahan enemy"""
        pass

    def enemy_pos_check(self):
        """
        Untuk mengubah arah enemy atau musuh ke arah berlawanan ketika dia telah menyentuh sisi layar. Kemudian memanggil method enemy_move_down untuk menggerakkan enemy ke bawah
        """
        pass

    def enemy_move_down(self):
        """Untuk menggerakan alien ke bawah dengan jarak tertentu"""
        pass

    def enemy_tembak_laser(self):
        """enemy_tembak_laser enemy dapat menembak player dengan ke tembakan random"""
        pass

    def display_lives(self):
        """ 
        Menampilkan lives atau nyawa yang dimiliki oleh player/pemain jika enemy berhasil membunuh pemain
        """
        pass

    def display_score(self):
        """ 
        Menampilkan Score yang dimiliki oleh player/pemain jika enemy berhasil membunuh pemain 
        """
        pass

    def game_result(self):
        """
        menampilkan hasil dari permainan, apakah player memenangkan permainan ataukah kalah dalam permainan
        """
        pass

    def run(self):
        """run untuk memanggil atribut yang telah dibuat sebelumnya"""
        pass


class enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        # self.color =  # menetapkan warna dari enemy
        # self.image =  # gambar atau bentuk dari enemy
        # self.rect = # objek box menempatkan enemy
        # self.value = # value dari tiap enemy untuk menambah score

    def update(self):
        """untuk menghapus jejak dari pergerakan enemy"""
        pass


class laser:
    def __init__(self):
        # self.velocity =
        # self.position =
        # self.Y_constraint = #gerakan vertikal dengan batasan laser untuk bergerak
        # ketika laser sudah melebihi batasan maka objek laser akan dihilangkan
        # self.image =
        # self.rect =
        pass

    def update(self):
        """untuk menghapus jejak dari pergerakan laser sekaligus mengerakkan laser dengan kecepatan yang ditentukan """
        pass


class player:
    def __init__(self):
        # self.velocity =
        # self.position =
        # self.xconstraint = # ger
        # self.image =
        # self.rect =
        # self.ready_boolean =
        self.laser_time = 0
        self.cooldown = 600
        # self.laser_sound =

    def gerak_player(self):
        """algoritma player bergerak ke kanan dan ke kiri dan serta menembakkan laser """
        pass

    def recharge_laser(self):
        """fungsi recharge berguna untuk mengatur jarak waktu laser ditembakkan"""
        pass

    def batas_player(self):
        """supaya gerakan player tidak melebihi batas layar"""
        pass

    def tembak_laser(self):
        """player tembak laser fungsi untuk menembakkan laser pada player saat player menekan tombol space"""
        pass

    def update(self):
        """untuk menghapus jejak dari pergerakan player"""
        pass
