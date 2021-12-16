package me.mix.myfirstplugin;

import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.inventory.InventoryClickEvent;

public class MenuHandeler implements Listener {
    @EventHandler
    public void onMenuClick(InventoryClickEvent e){
        Player p = (Player) e.getWhoClicked();
        if (e.getView().getTitle().equalsIgnoreCase(ChatColor.AQUA + "How shuld i kill him?")){
            e.setCancelled(true);
            if (e.getCurrentItem() == null){
                return;
            }
            if (e.getCurrentItem().getType().equals(Material.CHIPPED_ANVIL)){
                p.sendMessage("You want to slice someone! Nice!");
                p.closeInventory();
            } else if (e.getCurrentItem().getType().equals(Material.TNT)){
                p.sendMessage("You want to explode someone! Nice!");
                p.closeInventory();
            }
        }
    }
}
