package me.mix.customspellsplugin;

import org.bukkit.ChatColor;
import org.bukkit.Material;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

import java.util.ArrayList;

public class GenerateItems {
    public static ArrayList<ItemStack> allItems = new ArrayList<>();
    public static boolean hasListGenrated = false;

    public static void GenerateItemsToList(){
        allItems.add(getBook());
        allItems.add(getSpit());
        hasListGenrated = true;
    }
    public static boolean isAMagicalItem(ItemStack item){
        if (!hasListGenrated){
            GenerateItemsToList();
        }
        if (allItems.contains(item)){
            return true;
        } else {
            return false;
        }
    }

    public static ArrayList<ItemStack> getAllItems(){
        if (!hasListGenrated){
            GenerateItemsToList();
        }
        return allItems;
    }

    public static ItemStack getMagicalItem(Material item, String title, String[] lore){
        ItemStack magicItem = new ItemStack(item, 1);
        ItemMeta magicItemMeta = magicItem.getItemMeta();
        magicItemMeta.setDisplayName(title);
        magicItemMeta.setUnbreakable(true);
        magicItemMeta.addItemFlags(ItemFlag.HIDE_ATTRIBUTES);
        ArrayList<String> magicItemLore = new ArrayList<>();
        for (String i : lore) {
            magicItemLore.add(i);
        }
        magicItemMeta.setLore(magicItemLore);
        magicItem.setItemMeta(magicItemMeta);
        magicItem.addUnsafeEnchantment(Enchantment.DURABILITY, 255);

        return magicItem;
    }

    public static ItemStack getBook(){
        String[] lore = {ChatColor.DARK_AQUA + "Right click with this item to select a spell!"};
        ItemStack magicItem = getMagicalItem(Material.BOOK, ChatColor.GOLD + "Select a magic spell to use!", lore);

        return magicItem;
    }

    public static ItemStack getSpit(){
        String[] lore = {ChatColor.DARK_AQUA + "Right click with this item to select a spell!", ChatColor.DARK_AQUA + "Right click with this item to cast this spell!"};
        ItemStack magicItem = getMagicalItem(Material.CLAY_BALL, ChatColor.WHITE + "Spit on your opponents", lore);

        return magicItem;
    }
}
