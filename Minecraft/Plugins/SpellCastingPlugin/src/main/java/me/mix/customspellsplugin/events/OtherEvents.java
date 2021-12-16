package me.mix.customspellsplugin.events;

import me.mix.customspellsplugin.GenerateItems;
import me.mix.customspellsplugin.UseItems;
import org.bukkit.Material;
import org.bukkit.entity.Entity;
import org.bukkit.entity.LivingEntity;
import org.bukkit.entity.Player;
import org.bukkit.entity.Snowball;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.EntityDamageByEntityEvent;
import org.bukkit.event.entity.ProjectileHitEvent;
import org.bukkit.inventory.ItemStack;

public class OtherEvents implements Listener {
    @EventHandler
    private void onPlayerHit(EntityDamageByEntityEvent e){
        if (e.getDamager() instanceof Player){
            Player p = (Player) e.getDamager();
            ItemStack item1 = p.getInventory().getItemInMainHand();
            if (item1 != null && !item1.getType().equals(Material.AIR) && GenerateItems.isAMagicalItem(item1)){
                if (item1.equals(GenerateItems.getSpit())){
                    UseItems.spit(p);
                    e.setCancelled(true);
                }
            }
        }
        else if (e.getDamager() instanceof Snowball){
            Snowball s = (Snowball) e.getDamager();
            if (s.getCustomName().equals("An spit shot from the great spitter")){
                if (e.getEntity() instanceof LivingEntity){
                    LivingEntity entity = (LivingEntity) e.getEntity();
                    entity.damage(2);
                }
            }
        }
    }

}
