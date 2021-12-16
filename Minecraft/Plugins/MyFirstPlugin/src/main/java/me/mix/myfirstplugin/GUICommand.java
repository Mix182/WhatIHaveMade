package me.mix.myfirstplugin;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

public class GUICommand implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {

        if(sender instanceof Player){
            Player p = (Player) sender;

            Inventory gui = Bukkit.createInventory(p, 9, ChatColor.AQUA + "How shuld i kill him?");

            ItemStack i1 = new ItemStack(Material.CHIPPED_ANVIL, 1);
            ItemMeta i1Meta = i1.getItemMeta();
            i1Meta.setDisplayName("Slice");
            i1.setItemMeta(i1Meta);

            ItemStack i2 = new ItemStack(Material.TNT, 1);
            ItemMeta i2Meta = i2.getItemMeta();
            i2Meta.setDisplayName("Explode");
            i2.setItemMeta(i2Meta);

            gui.addItem(i1, i2);

            p.openInventory(gui);
        }

        return true;
    }
}
