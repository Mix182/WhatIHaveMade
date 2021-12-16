package me.mix.customspellsplugin;

import me.mix.customspellsplugin.commands.GivePlayerSpellsItemCommand;
import me.mix.customspellsplugin.events.GuiInteracteble;
import me.mix.customspellsplugin.events.OtherEvents;
import me.mix.customspellsplugin.events.onClcikEvent;
import org.bukkit.ChatColor;
import org.bukkit.plugin.java.JavaPlugin;

public final class CustomSpellsPlugin extends JavaPlugin {

    @Override
    public void onEnable() {
        // Plugin startup logic
        System.out.println("Custom spells plugin has started.");


        getCommand("givemagicalitem").setExecutor(new GivePlayerSpellsItemCommand());
        getServer().getPluginManager().registerEvents(new onClcikEvent(), this);
        getServer().getPluginManager().registerEvents(new GuiInteracteble(), this);
        getServer().getPluginManager().registerEvents(new OtherEvents(), this);
    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}
