package me.mix.customspellsplugin.commands;

import me.mix.customspellsplugin.GenerateItems;
import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.entity.Player;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

import java.util.ArrayList;

public class GivePlayerSpellsItemCommand implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (args.length == 0){
            if (sender instanceof Player){
                Player p = (Player) sender;
                GivePlayerMagicItem(p);
            } else {
                sender.sendMessage(ChatColor.RED + "You need to specify an player who you want to give ability to use these spells!!!");
            }
        } else if (args.length == 1){
            try{
                Player p = Bukkit.getServer().getPlayer(args[0]);
                GivePlayerMagicItem(p);
            }
            catch (Exception e){
                sender.sendMessage(ChatColor.RED + "The \"" + args[0] + "\" is not a valid player name, try it again with a valid one!");
            }
        } else {
            sender.sendMessage(ChatColor.RED + "This command takes only 0 or 1 arguments, not " + args.length + ", please try it again!");
        }

        return true;
    }
    public void GivePlayerMagicItem(Player player){
        ItemStack magicItem = GenerateItems.getBook();

        player.getInventory().addItem(magicItem);
    }
}
