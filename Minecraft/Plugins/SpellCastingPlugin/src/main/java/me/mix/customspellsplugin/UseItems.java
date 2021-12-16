package me.mix.customspellsplugin;

import org.bukkit.entity.Player;
import org.bukkit.entity.Snowball;

public class UseItems {
    public static void spit(Player player){
        Snowball arrow = player.launchProjectile(Snowball.class);
        arrow.setCustomName("An spit shot from the great spitter");
        arrow.setVelocity(player.getLocation().getDirection().multiply(0.5));
    }
}
