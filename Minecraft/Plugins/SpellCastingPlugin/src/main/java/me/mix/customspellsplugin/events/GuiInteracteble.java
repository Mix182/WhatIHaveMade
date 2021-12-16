package me.mix.customspellsplugin.events;

import me.mix.customspellsplugin.GenerateItems;
import org.bukkit.ChatColor;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.inventory.InventoryClickEvent;

public class GuiInteracteble implements Listener {
    @EventHandler
    public void onPlayerInventory(InventoryClickEvent e){
        Player p = (Player) e.getWhoClicked();
        if (e.getView().getTitle().equalsIgnoreCase(ChatColor.DARK_PURPLE + "Chose your spell!")){
            e.setCancelled(true);
            if (GenerateItems.isAMagicalItem(p.getInventory().getItemInMainHand())){
                if (!(e.getCurrentItem() == null) && GenerateItems.isAMagicalItem(e.getCurrentItem())){
                    p.getInventory().setItemInMainHand(e.getCurrentItem());
                    p.closeInventory();
                }
            } else {
                p.closeInventory();
            }
        }
    }
}
