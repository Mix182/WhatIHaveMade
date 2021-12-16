package me.mix.customspellsplugin.events;

import me.mix.customspellsplugin.GenerateItems;
import me.mix.customspellsplugin.UseItems;
import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.Action;
import org.bukkit.event.entity.EntityDamageByEntityEvent;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;

import java.util.ArrayList;

public class onClcikEvent implements Listener {
    @EventHandler
    public void onPlayerClcik(PlayerInteractEvent e) {
        if (e.getAction().equals(Action.RIGHT_CLICK_AIR) || e.getAction().equals(Action.RIGHT_CLICK_BLOCK)) {
            ItemStack item = e.getItem();
            if (item != null && !item.getType().equals(Material.AIR) && GenerateItems.isAMagicalItem(item)) {
                openInventory(e.getPlayer());
            } else {
                return;
            }
        }
        if (e.getAction().equals(Action.LEFT_CLICK_AIR) || e.getAction().equals(Action.LEFT_CLICK_BLOCK)){
            ItemStack item1 = e.getItem();
            if (item1 != null && !item1.getType().equals(Material.AIR) && GenerateItems.isAMagicalItem(item1)) {
                if (item1.equals(GenerateItems.getSpit())){
                    UseItems.spit(e.getPlayer());
                    e.setCancelled(true);
                }
            } else {
                return;
            }
        }
    }
    private void openInventory(Player p){
        ArrayList<ItemStack> magicalItems = GenerateItems.getAllItems();

        Inventory selectMenu = Bukkit.createInventory(p, (int) (Math.ceil(magicalItems.size() / 9.0) * 9), ChatColor.DARK_PURPLE + "Chose your spell!");
        selectMenu.setContents(magicalItems.toArray(new ItemStack[0]));

        p.openInventory(selectMenu);
    }
}
